##### flood.pub
- Composable
- Publish
- Subscribe
- High Velocity

##### Supported Formats
- Markdown
- json
- XML
- txt
- oembed

##### Todos

  [ ] Stand up production environment
  [ ] Point domain to production environment

##### Scaling

Keep an eye on:
  - dynamodb ReadCapacityUnits/WriteCapacityUnits
  - elasticbeantalk instances

##### Deploy

```bash
source venv/bin/activate
pip freeze >requirements.txt
deactivate
eb deploy
```

##### New Environment

```bash
source venv/bin/activate
pip freeze >app/requirements.txt
deactivate
eb init --region us-east-1
eb create
```

##### Dynamodb Local

*Installation*
```bash
brew install dynamodb-local

# run dynamo locally
/usr/local/bin/dynamodb-local

# shell
open http://localhost:8000/shell/

```

##### Research
http://pubpub.media.mit.edu/
https://octicons.github.com/
http://bulma.io/
