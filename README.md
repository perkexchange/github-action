# Perk.Exchange GitHub Action

Reward your developers and users with cryptocurrency using Perk.Exchange.

## Usage

Copy the example workflow below

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  reward:
    runs-on: ubuntu-latest

    steps:
        # Reward the initiating user with cryptocurrency       
      - uses: perkexchange/github-action@v0.3
        name: Perk.Exchange Reward
        with:
            apiToken: XXXXXXXXXXX
            campaignReference: YYYYYYYYYYY
            userId: ${{ github.event.sender.id }}
            amount: 3
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `apiToken`  | Perk.Exchange developer API token. Available here: https://perk.exchange/Developer    |
| `campaignReference`  | Public reference for campaign    |
| `userId`  | The user's internal Id    |
| `amount`  | Reward amount   |
| `platform` _(optional)_  | User platform: github (default), twitter, github, google, slack, discord    |

### Outputs

None

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!
