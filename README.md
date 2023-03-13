# Data Liberation Project: The Metadata 

This repository contains metadata about the [Data Liberation Project](https://www.data-liberation-project.org/)'s activities, generated from the same information that powers the DLP's website.

## Records requests

In [`data/requests.csv`](data/requests.csv), you can find metadata about each of the DLP's [records requests](https://www.data-liberation-project.org/requests/). The file contains the following fields:

| Column  | Description  | Example Value  |
|---------|--------------|----------------|
| slug  | The URL "slug" for the request, which also serves as a unique identifier.  | public-housing-inspections  |
| title  | The title of the request on the DLP's website.  | Public Housing Inspections  |
| agency  | The agency to which the request was sent, with agency hierarchies delimited by a &vert; character. | Department of Housing and Urban Development (HUD)&vert;Office of Public and Indian Housing (PIH)  |
| date  | The date the DLP submitted the request.  | 2022-09-23  |
| date_resubmitted  | The date the DLP re-submitted the request, if applicable.  | 2023-03-13  |
| status  | The current status of the request.  | Acknowledged  |
| request_id  | The tracking number the agency assigned to the request.  | 22-FI-HQ-01969  |
| last_updated | The date the DLP last updated the request status or noted an update.  | 2022-09-29  |
| request_letter  | A link to the request letter the DLP sent.  | [https://www.documentcloud.org/...](https://www.documentcloud.org/documents/22925204-2022-09-23-hud-phaspass-foia-request) |

## Records request updates 

In [`data/updates.csv`](data/updates.csv), you can find metadata about the updates that the DLP posts to the individual request pages. The file contains the following fields:

| Column  | Description  | Example Value  |
|---------|--------------|----------------|
| slug  | The DLP's request identifier. See `requests.csv` file above. | ssvf-satisfaction-surveys  |
| date  | The date of the update. | 2022-12-27  |
| title | The title of the update. | Fee Waiver Appeal Granted  |
| body  | The full update text, in Markdown. | On December 27, 2022, the VA's Office of General Counsel [emailed a letter 📄](https://www.documentcloud.org/documents/23557285-2022-12-27-singer-vine-162878-remand-letter) granting [...] |
