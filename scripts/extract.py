import argparse
import csv
import typing
from itertools import chain
from operator import itemgetter
from pathlib import Path

import frontmatter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("content_dir", type=Path)
    return parser.parse_args()


def filter_posts(path: Path) -> bool:
    return path.stem[0] != "_"


def req_to_row(path: Path) -> dict[str, str]:
    m = frontmatter.load(path).metadata
    max_update = max(
        [m["last_updated"]] + [u["date"].date() for u in m.get("updates", [])]
    )

    if m["last_updated"] < max_update:
        raise ValueError(f"Update dates out of sync for {path.stem}")

    return dict(
        slug=path.stem,
        title=m["title"],
        agency=m["agency"].replace(" ▹ ", "|"),
        date=m["date"].strftime("%Y-%m-%d"),
        status=m["status"],
        request_id=m["request_id"],
        last_updated=max_update.strftime("%Y-%m-%d"),
        request_letter=m["request_letter"],
    )


def req_to_update_rows(path: Path) -> typing.Generator[dict[str, str], None, None]:
    m = frontmatter.load(path).metadata
    for update in m.get("updates", []):
        update["date"] = update["date"].strftime("%Y-%m-%d")
        yield {"slug": path.stem, **update}


def extract_requests(content_dir: Path) -> list[dict[str, str]]:
    paths_all = content_dir.glob("*.md")
    paths_to_parse = filter(filter_posts, paths_all)
    extracted = map(req_to_row, paths_to_parse)
    s = reversed(sorted(extracted, key=itemgetter("date", "slug")))
    return list(s)


def extract_updates(content_dir: Path) -> list[dict[str, str]]:
    paths_all = content_dir.glob("*.md")
    paths_to_parse = filter(filter_posts, paths_all)
    extracted = chain(*map(req_to_update_rows, paths_to_parse))
    s = reversed(sorted(extracted, key=itemgetter("date", "slug")))
    return list(s)


def write(results: list[dict[str, str]], dest: Path) -> None:
    fieldnames = list(results[0].keys())
    with open(dest, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main() -> None:
    args = parse_args()

    requests = extract_requests(args.content_dir)
    write(requests, Path("data/requests.csv"))

    updates = extract_updates(args.content_dir)
    write(updates, Path("data/updates.csv"))


if __name__ == "__main__":
    main()
