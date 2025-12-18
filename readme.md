# Fruit App - Django Template Project

A Django web application for managing and displaying fruits with a modern, futuristic user interface. The application demonstrates Django templates, static files handling, and custom error pages.

## Features

- **Fruit Management**: Display fruits with name, color, weight, and images
- **Order Status**: Two-column layout separating ordered and non-ordered fruits
- **Modern UI**: Futuristic design with glassmorphism effects, gradients, and animations
- **Responsive Design**: Fully responsive layout that adapts to different screen sizes
- **Custom 404 Page**: Custom error page with background image
- **Static Files**: Organized CSS and image assets

## Technologies

- Python 3.x
- Django 6.0
- HTML5/CSS3
- Google Fonts (Inter)

## Project Structure

```
fruitsbackend2/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── fruit_app/
│   ├── static/
│   │   └── fruit_app/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── img/
│   │           ├── apfel.jpg
│   │           ├── banane.jpg
│   │           ├── birne.jpg
│   │           ├── kirsche.jpg
│   │           ├── orange.jpg
│   │           ├── logo.jpg
│   │           └── 4042.png
│   ├── templates/
│   │   └── fruit_app/
│   │       ├── base.html
│   │       ├── header.html
│   │       ├── fruitlist.html
│   │       ├── info.html
│   │       └── 404.html
│   ├── fruit_list.py
│   ├── views.py
│   └── urls.py
└── manage.py
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd fruitsbackend2
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure settings:
```bash
# For development, set DEBUG = True in core/settings.py
# For production, set DEBUG = False and configure ALLOWED_HOSTS
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
# Standard mode
python manage.py runserver

# With static files in DEBUG=False mode
python manage.py runserver --insecure
```

8. Open your browser and navigate to:
```
http://127.0.0.1:8000/fruit_app/
```

## Usage

### Main Pages

- /fruit_app/ - Main fruit list with ordered/not ordered columns
- /fruit_app/info/ - Information page
- Any invalid URL - Custom 404 error page

### Development Notes

- Static files are served automatically in development mode (DEBUG=True)
- For production deployment, collect static files using `python manage.py collectstatic`
- Custom 404 page only appears when DEBUG=False

## Configuration

### Adding New Fruits

Edit fruit_app/fruit_list.py:

```python
fruits = [
	{
		"name": "Apple",
		"weight": 100,
		"color": "red",
		"img": "fruit_app/img/apple.jpg",
		"ordered": False
	},
	# Add more fruits...
]
```

### Styling

Modify fruit_app/static/fruit_app/css/style.css to customize the design. The CSS uses CSS custom properties for easy theming:

```css
:root {
	--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
	--secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
	--bg-dark: #0a0e27;
	/* ... */
}
```

## License

This project is for educational purposes.

## Author

Created as part of a Django backend development course.
