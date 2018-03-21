# checkgip
Global IP Check, when if IP changed post Slack message.

## Requirements
tested with Linux (Raspberry pi) and macOSX 10.13

* Slack Account
* Slack Incomming Webhook
* python 2.7.x

## How to Install
* Install PIP.
* Clone this repository.
```
git clone https://github.com/thesaitama/checkgip.git
```   
* Install dependencies.
```
cd checkgip
pip install -r requirements.txt
```
* Configure JSON Settings file.
  + Rename sample JSON File.
  ```
  mv checkgip.sample.json checkgip.json
  ```
  + Edit checkgip.json
  ```
  {"slackWebhook": "<YOUR_SLACK_INCOMING_WEBHOOK>"}
  ```
  + Set write permission checkgip.json
    - script save previous global IP addr.
  ```
  chmod +w checkgip.json
  ```
  + Set crontab
  ```
  # m h  dom mon dow   command
  0 12 * * * python /<APP_DIR>/checkgip.py > /dev/null
  ```

## Links
* Slack - Incoming Webhooks
 https://api.slack.com/incoming-webhooks
* Qiita - SlackとRaspberry PiでグローバルIPアドレスの変更を通知
 https://qiita.com/thesaitama/items/7a3b0c7445dc276536fc

## Maintainer
* Kazuhiro Komiya

