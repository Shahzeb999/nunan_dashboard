from app import app, db
from app.models import Cell, CellData, CycleData, StatisticsData, DetailVoltageData, DetailTemperatureData #DetailData
from app.utils import process_excel_file as import_data

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Cell': Cell,
        'CellData': CellData,
        'CycleData': CycleData,
        'StatisticsData': StatisticsData,
        'DetailVoltageData': DetailVoltageData,
        'DetailTemperatureData': DetailTemperatureData
        #'DetailData': DetailData
    }

if __name__ == '__main__':
    # Create database tables and import data within application context
    with app.app_context():
        # db.drop_all()  # Drop all tables, optional
        db.create_all()
        # Import data
        # import_data('data/5308.xls')
        # import_data('data/5329.xls')

    # Run the Flask app
    app.run(port=3000, debug=True)
