# Perk.Exchange GitHub Action

Reward developers and users with cryptocurrency for performing certain actions. Rewards are provisioned by <https://perk.exchange>.

## Requirements

- **Enable access** We are in the test phase of this action. Please reach out to us on [Twitter](https://twitter.com/perkexchange) for access.

- **Users Register with Perk.Exchange** Users must first connect to https://perk.exchange with their GitHub user. Rewards are not provisioned for GitHub users that haven't already registered with Perk.Exchange.

## Usage

Store your Perk.Exchange **API Token** and **Campaign reference** in repository secrets. Use the example workflow below as a base and modify to suit your needs. You can also refer to this repository's workflow.

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
        # Reward the initiating user with cryptocurrency       
      - uses: perkexchange/github-action@v0.7-alpha
        name: Perk.Exchange Reward
        with:
            apiToken: ${{ secrets.PERKEXCHANGE_APITOKEN }}
            campaignReference: ${{ secrets.PERKEXCHANGE_CAMPAIGNREFERENCE }}
            userId: ${{ github.event.sender.id }}
            amount: 3
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `apiToken`  | Perk.Exchange developer API token. Once enabled, available here: https://perk.exchange/Developer Store in a repo secret    |
| `campaignReference`  | A string reference that uniquely identifies your campaign (Perk) - Store in a repo secret |
| `userId`  | The user's internal Id    |
| `amount`  | Reward amount   |
| `platform` _(optional)_  | User platform: github (default), twitter, github, google, slack, discord    |

### Outputs

None

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!

## Sponsorship

We can connect your brand with developers using Perk.Exchange. Please DM us on [Twitter](https://twitter.com/perkexchange) for more details.
