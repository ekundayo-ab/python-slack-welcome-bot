# Slack Welcome Bot

A slack bot implemented in python for welcoming new users to a slack team. This implementation uses __Python 3__

## Getting Started

To get this app working on a slack team follow these steps
1. Create a slack team [here](https://slack.com/get-started#create)
2. Create a new slack bot [here](https://dynamicindex.slack.com/apps/new/A0F7YS25R-bots)
3. Add the **Bots** Features and functionality for the just created app
4. Fill out the **Bot** Details
5. On the next page copy out the **API Token** and fill out other details as needed
6. Click **Save Integration**

### Prerequisites

- Python 3 with pip
- virtualenv
- slackclient

```
1. Check out how to install python 3 here
2. For virtualenv `pip install virtualenv`
3. For slackclient `pip install slackclient`
```

### Installing

To install and get running locally
1. run command `pip install virtualenv`
2. run command `pip install -r requirements.txt`
3. Set API Token gotten from slack as _SLACK_BOT_TOKEN_ in your os environment
4. Update Channel ID you need bot to function in the `starterbot.py` file in the project's root directory
5. `cd` into project root directory and run command `python starterbot.py`
6. Test out bot in the slack teaminished

## Running the tests

N/A

### Break down into end to end tests

N/A

### And coding style tests

N/A

## Deployment

N/A

## Built With

* [python-slackclient](https://github.com/slackapi/python-slackclient) - The web framework used
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) - Dependency Management

## Contributing

N/A

## Versioning

N/A

## Authors

* **Ekundayo Abiona** [Github Profile](https://github.com/ekundayo-ab)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

N/AA
