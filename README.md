# CryptoTicker
Lightweight browser bitcoin price ticker.  Implemented with a simple static page served up by api gateway.

Try it out: https://aq4snxo2ri.execute-api.us-west-2.amazonaws.com/prod/ticker

Or deploy yourself.

# Workspace prep

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

# Building

```
$ cdk synth
```

# Deploying

```
$ cdk diff --profile zzz
```
```
$ cdk deploy --profile zzz
```
