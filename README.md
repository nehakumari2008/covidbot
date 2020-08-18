# India Covid Stats Bot

This is a bot that answers the following:

* Country wise COVID stats
* State & City wise COVID stats for India

This bot is configured to use `Telegram`. Since we are using [Errbot](https://github.com/errbotio/errbot) you can also use `Slack`, `Hipchat`, `IRC` etc. Please see `Errbot` page for more information.

## Installation

### Configure the Telegram Backend
Create a file called `token.txt` in the pybot directory. Put your Telegram token without any spaces or `"` in this file.

To know how to create a telegram token please see [Bothfather Tutorial](https://core.telegram.org/bots#6-botfather).

### Using Local Machine
```bash
pip install -r requirements.txt
errbot
```

### Using Docker

```bash
docker-compose up
```

## Using the Bot

At this point go to the telegram bot you have created and talk to it.

`!covid <Country|Indian State|Indian City>`

![Using the Bot](https://user-images.githubusercontent.com/69853711/90517979-c62c9f80-e183-11ea-8a03-e7e3a5051549.jpg )

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)