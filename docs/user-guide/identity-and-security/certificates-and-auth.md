# File Pickers, Sign-in & System Prompts

A website may need a file, a login, a certificate or permission before you can continue. Read the site and requested action in the prompt before choosing an answer. These questions appear outside the web page, so they may also explain why an agent seems to be waiting.

## Choose a file

Uploads and Save As use Windows file dialogs. Choose the file or destination as usual, or cancel to return to the page. An agent can also select upload files directly or operate a supported open file dialog.

## Sign in to a server

The **Sign in** dialog identifies the site and the area requesting authentication. Choose a **Saved login** from the password vault, or enter **User name** and **Password**. **Save in password vault** stores the login for later use. The dialog warns when the connection is not encrypted.

This is server authentication, which can appear before a website's own login page. Cancel if you did not expect the request.

## Handle certificate questions

**Connection is not secure** means Nova could not validate the website's certificate. **Show details** lets you inspect it. **Go back** refuses the connection; **Continue anyway** makes an exception for that certificate in the current profile until Nova closes. It does not permanently trust the certificate.

**Identify yourself?** is a different question: the server requests a client certificate from you. Choose **Send selected** only for the identity you intend to use, or **Send none**.

## Answer a permission request

For supported device requests, **Allow once** gives temporary access, **Always allow** remembers a decision, and **Block** refuses it. Some requests also ask which device to use. Review saved choices in [Permissions](permissions.md).

For a runnable download, **Keep this file?** offers **Keep** or **Discard**. See [Download safety](../browser/downloads.md#3-executable-files-keep-this-file). Keeping a file does not establish that it is safe to run.

## When an agent is working

Agents can inspect and answer supported prompts too. A prompt is not necessarily waiting for a human-only approval. If you want to interrupt agent work before deciding, use [Emergency stop](../agents/taking-over-and-emergency-stop.md#3-staying-in-control).

For the agent-facing interfaces, use the [MCP reference](../../mcp-reference/README.md). For background, see [Native dialogs and prompts](../../core-features/native-dialogs-and-prompts/README.md).

[Back to this section](README.md) · [All user guides](../README.md)
