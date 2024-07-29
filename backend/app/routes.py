from flask import jsonify, request
from app import app, db
from app.models import CycleData, StatisticsData, DetailVoltageData, DetailTemperatureData, CellData, DetailData
from app.utils import process_excel_file

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        file_path = f"data/{file.filename}"
        file.save(file_path)
        process_excel_file(file_path)
        return jsonify({"success": "File processed successfully"})

@app.route('/cycle_data', methods=['GET'])
def get_cycle_data():
    data = CycleData.query.all()
    return jsonify([{
        'id': d.id,
        'channel': d.channel,
        'total_cycle': d.total_cycle,
        'charge_capacity': d.charge_capacity,
        'discharge_capacity': d.discharge_capacity,
        'cycle_life': d.cycle_life,
        'filename': d.filename
    } for d in data])

@app.route('/statistics_data', methods=['GET'])
def get_statistics_data():
    data = StatisticsData.query.all()
    return jsonify([{
        'id': d.id,
        'channel': d.channel,
        'cycle': d.cycle,
        'step': d.step,
        'status': d.status,
        'start_voltage': d.start_voltage,
        'end_voltage': d.end_voltage,
        'start_current': d.start_current,
        'end_current': d.end_current,
        'capacity': d.capacity,
        'endure_time': d.endure_time,
        'relative_time': d.relative_time,
        'absolute_time': d.absolute_time,
        'discharge_capacity_1': d.discharge_capacity_1,
        'charge_capacity': d.charge_capacity,
        'discharge_capacity_2': d.discharge_capacity_2,
        'net_energy_discharge': d.net_energy_discharge,
        'energy_charge': d.energy_charge,
        'energy_discharge': d.energy_discharge,
        'filename': d.filename
    } for d in data])

@app.route('/detail_voltage_data', methods=['GET'])
def get_detail_voltage_data():
    data = DetailVoltageData.query.all()
    return jsonify([{
        'id': d.id,
        'record_id': d.record_id,
        'step_name': d.step_name,
        'relative_time': d.relative_time,
        'realtime': d.realtime,
        'auxiliary_channel_voltage': d.auxiliary_channel_voltage,
        'gap_of_voltage': d.gap_of_voltage,
        'filename': d.filename
    } for d in data])

@app.route('/detail_temperature_data', methods=['GET'])
def get_detail_temperature_data():
    data = DetailTemperatureData.query.all()
    return jsonify([{
        'id': d.id,
        'record_id': d.record_id,
        'step_name': d.step_name,
        'relative_time': d.relative_time,
        'realtime': d.realtime,
        'auxiliary_channel_temperature': d.auxiliary_channel_temperature,
        'gap_of_temperature': d.gap_of_temperature,
        'filename': d.filename
    } for d in data])

@app.route('/current_data/<filename>', methods=['GET'])
def get_current_data(filename):
    full_filename = f"{filename}.xls"
    data = DetailData.query.filter_by(filename=full_filename).all()
    return jsonify([{
        'cycle': d.cycle,
        'step': d.step,
        'cur': d.cur,
        'filename': d.filename
    } for d in data])

@app.route('/voltage_data/<filename>', methods=['GET'])
def get_voltage_data(filename):
    full_filename = f"{filename}.xls"
    data = DetailData.query.filter_by(filename=full_filename).all()
    return jsonify([{
        'cycle': d.cycle,
        'step': d.step,
        'voltage': d.voltage,
        'filename': d.filename
    } for d in data])

@app.route('/capacity_data/<filename>', methods=['GET'])
def get_capacity_data(filename):
    full_filename = f"{filename}.xls"
    data = DetailData.query.filter_by(filename=full_filename).all()
    return jsonify([{
        'cycle': d.cycle,
        'step': d.step,
        'capacity': d.capacity,
        'filename': d.filename
    } for d in data])

@app.route('/temperature_data/<filename>', methods=['GET'])
def get_temperature_data(filename):
    full_filename = f"{filename}.xls"
    data = DetailTemperatureData.query.filter_by(filename=full_filename).all()
    return jsonify([{
        'record_id': d.record_id,
        'step_name': d.step_name,
        'relative_time': d.relative_time,
        'realtime': d.realtime,
        'auxiliary_channel_temperature': d.auxiliary_channel_temperature,
        'gap_of_temperature': d.gap_of_temperature,
        'filename': d.filename
    } for d in data])

@app.route('/api/cell-data/<filename>', methods=['GET'])
def get_cell_data(filename):
    full_filename = f"{filename}.xls"
    current_data = [data.cur for data in DetailData.query.filter_by(filename=full_filename).all()]
    voltage_data = [data.voltage for data in DetailData.query.filter_by(filename=full_filename).all()]
    capacity_data = [data.capacity for data in DetailData.query.filter_by(filename=full_filename).all()]
    temperature_data = [data.auxiliary_channel_temperature for data in DetailTemperatureData.query.filter_by(filename=full_filename).all()] 
    time_data = [data.absolute_time for data in DetailData.query.filter_by(filename=full_filename).all()]

    return jsonify({
        'currentData': current_data,
        'voltageData': voltage_data,
        'capacityData': capacity_data,
        'temperatureData': temperature_data,
        'timeData': time_data,
    })

# New routes for verifying data
@app.route('/verify/cycle_data', methods=['GET'])
def verify_cycle_data():
    data = CycleData.query.all()
    return jsonify([{
        'id': d.id,
        'channel': d.channel,
        'total_cycle': d.total_cycle,
        'charge_capacity': d.charge_capacity,
        'discharge_capacity': d.discharge_capacity,
        'cycle_life': d.cycle_life,
        'filename': d.filename
    } for d in data])

@app.route('/verify/statistics_data', methods=['GET'])
def verify_statistics_data():
    data = StatisticsData.query.all()
    return jsonify([{
        'id': d.id,
        'channel': d.channel,
        'cycle': d.cycle,
        'step': d.step,
        'status': d.status,
        'start_voltage': d.start_voltage,
        'end_voltage': d.end_voltage,
        'start_current': d.start_current,
        'end_current': d.end_current,
        'capacity': d.capacity,
        'endure_time': d.endure_time,
        'relative_time': d.relative_time,
        'absolute_time': d.absolute_time,
        'discharge_capacity_1': d.discharge_capacity_1,
        'charge_capacity': d.charge_capacity,
        'discharge_capacity_2': d.discharge_capacity_2,
        'net_energy_discharge': d.net_energy_discharge,
        'energy_charge': d.energy_charge,
        'energy_discharge': d.energy_discharge,
        'filename': d.filename
    } for d in data])

@app.route('/verify/detail_voltage_data', methods=['GET'])
def verify_detail_voltage_data():
    data = DetailVoltageData.query.all()
    return jsonify([{
        'id': d.id,
        'record_id': d.record_id,
        'step_name': d.step_name,
        'relative_time': d.relative_time,
        'realtime': d.realtime,
        'auxiliary_channel_voltage': d.auxiliary_channel_voltage,
        'gap_of_voltage': d.gap_of_voltage,
        'filename': d.filename
    } for d in data])

@app.route('/verify/detail_temperature_data', methods=['GET'])
def verify_detail_temperature_data():
    data = DetailTemperatureData.query.all()
    return jsonify([{
        'id': d.id,
        'record_id': d.record_id,
        'step_name': d.step_name,
        'relative_time': d.relative_time,
        'realtime': d.realtime,
        'auxiliary_channel_temperature': d.auxiliary_channel_temperature,
        'gap_of_temperature': d.gap_of_temperature,
        'filename': d.filename
    } for d in data])
