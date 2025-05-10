# <img src="https://img.icons8.com/color/48/000000/twitter.png" width="32" height="32"/> Ta3meya Chat

> **A Twitter-like social media platform built with Django**

[![Django](https://img.shields.io/badge/Django-4.1-092E20?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)](https://www.sqlite.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-2.0-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
[![jQuery](https://img.shields.io/badge/jQuery-3.5-0769AD?logo=jquery)](https://jquery.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![Ta3meya Chat Demo](https://placehold.co/800x400/22c55e/FFFFFF/png?text=Ta3meya+Chat&font=montserrat)

## 🌟 Overview

Ta3meya Chat is a social media platform built with Django, offering Twitter-like functionality with a focus on user interactions. Users can create profiles, share posts, follow other users, engage with content through likes, and communicate via direct messaging.

<b>🔑 Key Features</b>

- 👤 **User Authentication** - Secure signup, login, and account management
- 📝 **Post Creation** - Share text updates with image and video support
- 🔄 **Timeline Feed** - View posts from followed users in a chronological feed
- 👥 **Follow System** - Follow/unfollow users to customize your feed
- ❤️ **Engagement** - Like and interact with posts
- 💬 **Direct Messaging** - Private conversations between users
- 🔍 **Search Functionality** - Find users across the platform
- 📊 **Trending Topics** - Discover popular content and discussions
- 📱 **Responsive Design** - Modern UI that works on all devices
- ✅ **Verification Badges** - Distinguished verified user accounts

## 🔧 Tech Stack

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="48" height="48" />
        <br/>Python
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" width="48" height="48" />
        <br/>Django
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" width="48" height="48" />
        <br/>SQLite
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" width="48" height="48" />
        <br/>HTML5
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" width="48" height="48" />
        <br/>CSS3
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" width="48" height="48" />
        <br/>JavaScript
      </td>
    </tr>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-plain.svg" alt="TailwindCSS" width="48" height="48" />
        <br/>TailwindCSS
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jquery/jquery-original.svg" alt="jQuery" width="48" height="48" />
        <br/>jQuery
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" width="48" height="48" />
        <br/>Git
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" alt="npm" width="48" height="48" />
        <br/>npm
      </td>
      <td align="center" width="96">
        <img src="https://cdn.worldvectorlogo.com/logos/font-awesome-1.svg" alt="Font Awesome" width="48" height="48" />
        <br/>Font Awesome
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="VS Code" width="48" height="48" />
        <br/>VS Code
      </td>
    </tr>
  </table>
</div>

<b>🖥️ Backend</b>

- Django 4.1 - High-level Python web framework
- Python 3.x - Programming language
- SQLite - Lightweight database for data storage
- Django ORM - Object-relational mapper for database interactions

<b>🎨 Frontend</b>

- HTML5 - Structure for web pages
- CSS3 - Styling and layout
- JavaScript - Client-side scripting
- TailwindCSS - Utility-first CSS framework
- jQuery - JavaScript library for DOM manipulation
- Font Awesome - Icon toolkit

## 📂 Project Structure

```
ta3meya-chat/
├── base/                   # Main application code
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Admin panel configuration
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View controllers
├── media/                  # User-uploaded content
│   ├── profile_images/     # User profile pictures
│   ├── profile_covers/     # User profile covers
│   └── post_images/        # Images for posts
├── static/                 # Static files
│   ├── assets/             # General assets
│   ├── css/                # CSS stylesheets
│   ├── dist/               # Compiled assets
│   ├── js/                 # JavaScript files
│   └── images/             # Static images
├── templates/              # HTML templates
│   ├── design/             # UI components
│   └── main/               # Main page templates
├── twitter/                # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
└── db.sqlite3              # SQLite database
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/yourusername/ta3meya-chat.git
cd ta3meya-chat
```

2️⃣ **Create and activate a virtual environment:**
```sh
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install dependencies:**
```sh
pip install django pillow
```

4️⃣ **Apply migrations:**
```sh
python manage.py migrate
```

5️⃣ **Create a superuser:**
```sh
python manage.py createsuperuser
```

6️⃣ **Run the development server:**
```sh
python manage.py runserver
```

7️⃣ **Open your browser:**
Navigate to `http://127.0.0.1:8000`

## 🌐 Features in Detail

### User Management
- **Profile Creation** - Create personalized profiles with profile pictures, cover photos, and bio information
- **Account Settings** - Customize user experience with profile settings
- **Verification System** - Distinguished verified accounts with badge display

### Content Sharing
- **Post Creation** - Share thoughts, images, and videos with followers
- **Media Support** - Upload and display images and videos in posts
- **Timeline Feed** - Chronological display of posts from followed users

### Social Interaction
- **Follow System** - Follow other users to see their content in your feed
- **Like System** - Engage with posts by liking them
- **Direct Messaging** - Private conversations between users with real-time updates

### Discovery
- **Search** - Find users across the platform
- **Trending Topics** - Discover popular discussions and content
- **User Suggestions** - Recommendations for new accounts to follow

### User Interface
- **Responsive Design** - Optimized for desktop and mobile devices
- **Dark Mode** - Comfortable viewing experience
- **Modern UI** - Clean, Twitter-inspired interface using TailwindCSS

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Django community for the powerful web framework
- TailwindCSS for the utility-first CSS framework
- Font Awesome for the icon toolkit
- All contributors who have helped shape this project

---

<div align="center">
  <img src="https://img.icons8.com/color/48/000000/twitter.png" width="24" height="24"/>
  <p>Connect with friends and share your thoughts with Ta3meya Chat</p>
</div> 
