import sys
from PyQt5.QtWidgets import QApplication
from test import CalculatorPage
from testb import DisplayPage

def main():
    app = QApplication(sys.argv)
    calculator_page = CalculatorPage()
    display_page = DisplayPage("No result passed")  # Pass a default value for result

    def show_display_page(result):
        calculator_page.hide()  # Hide calculator page
        display_page.display_result(result)
        display_page.show()  # Show display page

    calculator_page.next_page_signal.connect(show_display_page)
    calculator_page.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
