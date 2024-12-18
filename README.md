# Perk.Exchange GitHub Action

Add a donation button to your pull requrests. Donations are handled by <https://perk.exchange> using <https://getcode.com>.

## Detailed Instructions

- Go to <https://docs.perk.exchange/integrations/github> for detailed instructions.

## Requirements

- **Unlock** integrations on your <https://perk.exchange/Account> page.

- **Generate an API token** on the <https://perk.exchange/Integrations> page.

## Usage

Store your Perk.Exchange **API token** in a repository secret. Use the example workflow below as a base and modify to suit your needs. You can also refer to this repository's workflow.

**IMPORTANT**: Secrets are not passed to workflows that are triggered by a pull request from a fork. https://docs.github.com/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets

### Example workflow

```yaml
name: My Workflow
on:
  pull_request:
    types: [ closed ]
jobs:
  reward:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest

    steps:
        # Create donation button for this PR
      - uses: perkexchange/github-action@v0.15-alpha
        name: Perk.Exchange Donation Button
        with:
            apiToken: ${{ secrets.PERKEXCHANGE_APITOKEN }}
            currency: "USD"
            amount: 1
```
### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `apiToken`  | Integration api token - Store in a repo secret |
| `amount`  _(optional)_ | Donation amount (default is 1)  |
| `currency` _(optional)_  | Currency (default is "USD")    |
| `orderId` _(optional)_  | Unique payment identifier (default = "{owner}/{repo}/{branch}")    |
| `memo` _(optional)_  | Donation memo (default includes {repo_name} and {pr_url})    |

### Outputs

None

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!

## Sponsorship

Please DM us on [X](https://x.com/perkexchange) for more details.
