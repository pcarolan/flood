###### flood.pub
- Composable
- Publish
- Subscribe
- High Velocity

###### Supported Formats
- Markdown
- json
- XML
- txt
- oembed

###### Deploy

```bash
source venv/bin/activate
pip freeze >requirements.txt
deactivate
eb deploy
```

###### New Environment

```bash
source venv/bin/activate
pip freeze >app/requirements.txt
deactivate
eb init --region us-east-1
eb create
```

###### Research
http://pubpub.media.mit.edu/
https://octicons.github.com/
http://bulma.io/
