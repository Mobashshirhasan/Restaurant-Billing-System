# Restaurant Billing System

A Flask-based web application for managing restaurant orders and generating PDF invoices for Indian street food and cuisine items.

## Features

* Simple and intuitive web interface for order management
* Real-time order tracking
* Automated PDF invoice generation
* Pre-configured menu with popular Indian dishes
* Payment processing with change calculation

## Menu Items

The system includes the following items with their respective prices:

* Samosa: $10
* Vada Pav: $10
* Pani Puri/Golgappa: $20
* Bhel Puri: $30
* Chole Bhature: $75
* Pav Bhaji: $65
* Dosa: $65
* Idli: $40
* Chaat: $35
* Pakora: $35

## Technologies Used

* Python 3.x
* Flask (Web Framework)
* ReportLab (PDF Generation)
* HTML/CSS (Frontend)
* BytesIO (PDF Buffer Management)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/restaurant-billing-system.git
cd restaurant-billing-system
```

2. Install the required dependencies:
```bash
pip install flask reportlab
```

3. Run the application:
```bash
python app.py
```

4. Access the application in your web browser at `http://localhost:5000`

## Usage

1. Select items from the menu and specify quantities
2. Click "Add to Order" to include items in the current order
3. Enter the payment amount
4. Generate and download the PDF invoice

## Project Structure

```
restaurant-billing-system/
├── app.py              # Main application file
├── templates/          # HTML templates
│   └── index.html     # Main page template
├── static/            # Static files (CSS, JS)
└── README.md          # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact [your-email@example.com]

## Acknowledgments

* Thanks to all contributors who have helped with the development
* Inspired by the need for simple and efficient restaurant billing solutions
