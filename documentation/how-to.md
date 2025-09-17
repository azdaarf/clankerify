# How to
## Setup
### Python
#### In Windows

Open up a powershell window (see [Run: In Windows](#run-in-windows))
Run the following command:

```shell
python3
```
It should open up a Microsoft Store page for Python3 where you can click 'Get' to install it on your computer.

![microsoft store](/documentation/microsoft-store.png)

After installing python make sure you're standing in the root directory of this repo (if you aren't, follow the instructions in [Run: In Windows](#run-in-windows)) and run the following command:

```shell
pip install -r .\src\requirements.txt
```

When you're done with this step you should be done with all python prerequisites!

### Get an LLM API key
Currently only gemini is supported.

#### Gemini

See [Google's own documentation](https://ai.google.dev/gemini-api/docs/api-key)

### Clankerify

To set up Clankerify you need to:
- Add your CV to upload/profiles/active/
- Create a .env file in src/. You can copy the '.envexample' file and add your own api and app keys.
- Run Clankerify for the first time. See [Run: In Windows](#run-in-windows)

## Run
<a id="run-in-windows"></a>

### In Windows 10

Open up a powershell window by navigating to this repo's folder and hold down shift and right click. You should see a context menu looking something like this:

![windows 10 context menu](/documentation/open-powershell-window-here-w10.png)

Choose the alternative underlined in red.

Then run the following command:

```shell
python3 .\src\clankerify.py
```

### In Windows 11

Open up a powershell window by navigating to this repo's folder and  right click. You should see a context menu looking something like this: 

![windows 11 context menu](/documentation/open-in-terminal-w11.png)

Choose the alternative underlined in red.

Then run the following command:

```shell
python3 .\src\clankerify.py
```
