# 🏠 Roommate CLI

Your Personal AI Roommate - A beautiful command-line interface for chatting with your AI companion.

## ✨ Features

- 🎨 **Beautiful Terminal UI**: Rich, colorful interface with live streaming responses
- 💬 **Real-time Chat**: Stream responses as they're generated for a natural conversation flow
- 🔐 **Flexible Authentication**: Works with both public and private servers
- ⚡ **Fast & Responsive**: Optimized for speed with async streaming
- 🎭 **Typewriter Effect**: Smooth, engaging display of final responses
- 🌐 **Remote & Local Support**: Connect to the public API or run your own server

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/TheusHen/roommate-cli.git
cd roommate-cli

# Install required packages
pip install -r requirements.txt
```

Alternatively, you can install the dependencies manually:

```bash
pip install rich requests
```

## 🚀 Usage

### Basic Usage

Simply run the main script:

```bash
python main.py
```

### Authentication Options

#### Public Server (Default)
By default, the CLI connects to the public server at `https://roommate.theushen.me` with limited access (3 messages in test mode).

#### Private Server (Unlimited Access)
For unlimited access, create a configuration file with your API password:

1. Create a `config` directory in the parent folder:
   ```bash
   mkdir -p ../config
   ```

2. Add your API password to the file:
   ```bash
   echo "your-api-password-here" > ../config/api_password.txt
   ```

### Chat Commands

- **Chat**: Simply type your message and press Enter
- **Exit**: Type `exit`, `quit`, `:q`, `bye`, or `sair` to quit
- **Cancel**: Press `Ctrl+C` during a response to cancel (press twice to exit)

## 🎯 Examples

```
You: What's the weather like today?
[Roommate streams response in real-time]

You: Tell me a joke
[Roommate responds with humor]

You: exit
[Goodbye message]
```

## 🛠️ Configuration

The application uses the following configuration:

- **API URL**: `https://roommate.theushen.me` (default public server)
- **Config Directory**: `../config/` (relative to main.py)
- **Password File**: `../config/api_password.txt` (optional, for unlimited access)

## 📋 Requirements

- `rich>=13.0.0` - For beautiful terminal formatting
- `requests>=2.31.0` - For HTTP requests to the API

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Connection Issues

If you get a "Cannot connect to the Roommate server" error:

1. Check your internet connection
2. Verify the API server is online
3. If using a private server, ensure the URL is correct and accessible

### Import Errors

If you get import errors for `rich` or `requests`:

```bash
pip install --upgrade rich requests
```

## 🌟 Features in Detail

### Live Streaming
The CLI provides real-time streaming of AI responses, showing you the message as it's being generated, just like modern AI chat interfaces.

### Rich Terminal UI
Built with the `rich` library, Roommate offers:
- Markdown rendering for formatted responses
- Colorful panels and borders
- Spinner animations while waiting
- Clean, professional appearance

### Smart Input Handling
- Handles empty inputs gracefully
- Multiple exit command options
- Keyboard interrupt handling
- EOF detection

## 🔮 Future Plans

- [ ] Conversation history
- [ ] Multi-language support
- [ ] Custom themes
- [ ] Plugin system
- [ ] Voice input/output
- [ ] Context persistence

## 👨‍💻 Author

**I'm Matheus** (TheusHen)
- GitHub: [@TheusHen](https://github.com/TheusHen)

## 🙏 Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) for terminal formatting
- Powered by AI technology

---

Made with ❤️ by TheusHen
