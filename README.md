# 🎵 Billboard to Spotify Playlist Creator

A Python script that scrapes the Billboard Hot 100 chart for any given date and automatically creates a Spotify playlist with those songs.

## ✨ Features

- 📊 Scrapes Billboard Hot 100 chart for any date
- 🎧 Automatically searches for songs on Spotify
- 📝 Creates a private Spotify playlist with found songs
- 🔐 Secure credential management with environment variables
- ✅ Clean output showing which songs were found/not found

## 🛠️ Prerequisites

- Python 3.7 or higher
- Spotify Developer Account
- Spotify Premium (required for playlist creation)

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/albinjoby/Billboard-To-Spotify.git
   cd Billboard-To-Spotify
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Spotify App**

   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Note your `Client ID` and `Client Secret`
   - Add `https://albinjoby.vercel.app/` to Redirect URIs in your app settings

4. **Create environment file**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your Spotify credentials:

   ```
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   ```

## 🚀 Usage

Run the script and enter a date when prompted:

```bash
python main.py
```

**Example:**

```
enter the data in this format YYYY-MM-DD: 2004-09-24
```

The script will:

1. Scrape the Billboard Hot 100 for that date
2. Search for each song on Spotify
3. Create a private playlist named "BillBoard 100 [DATE]"
4. Add all found songs to the playlist

## 📁 Project Structure

```
billboard-to-spotify/
├── main.py              # Main script
├── test.py              # Testing script for Spotify API
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore file
├── token.txt           # OAuth token cache (auto-generated)
└── README.md           # This file
```

## 📋 Dependencies

- `beautifulsoup4` - Web scraping
- `requests` - HTTP requests
- `spotipy` - Spotify Web API wrapper
- `python-dotenv` - Environment variable management

## 🔧 Configuration

### Environment Variables

Create a `.env` file with your Spotify app credentials:

```env
CLIENT_ID=your_spotify_client_id_here
CLIENT_SECRET=your_spotify_client_secret_here
```

### Spotify OAuth Settings

The script uses these OAuth settings:

- **Scope**: `playlist-modify-private` (to create private playlists)
- **Redirect URI**: `https://albinjoby.vercel.app/`
- **Cache**: Tokens stored in `token.txt`

## 🎯 Example Output

```
enter the data in this format YYYY-MM-DD: 2004-09-24
your_spotify_user_id
Goodies found
Lean Back found
Sunshine found
My Place not found
She Will Be Loved found
...
Created playlist: BillBoard 100 2004-09-24
songs were sucessfully added
```

## 🚨 Troubleshooting

### Common Issues

1. **"No songs were added"**

   - Check if the date has a valid Billboard chart
   - Ensure your Spotify credentials are correct

2. **Authentication errors**

   - Verify your `CLIENT_ID` and `CLIENT_SECRET` in `.env`
   - Make sure redirect URI is added to your Spotify app

3. **Import errors**

   - Install all dependencies: `pip install -r requirements.txt`

4. **Billboard scraping issues**
   - Try a different date (some very recent dates might not have charts)
   - Check your internet connection

## 🔒 Security

- ✅ Credentials stored in `.env` file
- ✅ `.env` and `token.txt` ignored by Git
- ✅ OAuth tokens cached locally
- ✅ Private playlists created by default

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is for educational purposes. Please respect Billboard's and Spotify's terms of service.

## 🙏 Acknowledgments

- [Billboard.com](https://www.billboard.com) for the Hot 100 charts
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) for music data
- [Spotipy](https://spotipy.readthedocs.io/) for the excellent Python wrapper

## 📧 Contact

Albin Joby - [@albinjoby](https://github.com/albinjoby)

Project Link: [https://github.com/albinjoby/Billboard-To-Spotify](https://github.com/albinjoby/Billboard-To-Spotify)

---

⭐ If you found this project helpful, please give it a star!
