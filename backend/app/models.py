from app import db

class Cell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Float, nullable=False)
    chemistry = db.Column(db.String(50), nullable=False)
    voltage = db.Column(db.Float, nullable=False)
    filename = db.Column(db.String(100), nullable=False)

class CellData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'), nullable=False)
    cycle = db.Column(db.Integer, nullable=False)
    step = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    start_voltage = db.Column(db.Float, nullable=False)
    end_voltage = db.Column(db.Float, nullable=False)
    start_current = db.Column(db.Float, nullable=False)
    end_current = db.Column(db.Float, nullable=False)
    capacity = db.Column(db.Float, nullable=False)
    energy = db.Column(db.Float, nullable=False)
    relative_time = db.Column(db.String(50), nullable=False)
    absolute_time = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    
    cell = db.relationship('Cell', back_populates='data')

Cell.data = db.relationship('CellData', order_by=CellData.id, back_populates='cell')

class CycleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.Integer)
    total_cycle = db.Column(db.Integer)
    charge_capacity = db.Column(db.Float)
    discharge_capacity = db.Column(db.Float)
    cycle_life = db.Column(db.Float)
    filename = db.Column(db.String(100), nullable=False)

class StatisticsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.Integer)
    cycle = db.Column(db.Integer)
    step = db.Column(db.Integer)
    status = db.Column(db.String(50))
    start_voltage = db.Column(db.Float)
    end_voltage = db.Column(db.Float)
    start_current = db.Column(db.Float)
    end_current = db.Column(db.Float)
    capacity = db.Column(db.Float)
    endure_time = db.Column(db.String(50))
    relative_time = db.Column(db.String(50))
    absolute_time = db.Column(db.String(50))
    discharge_capacity_1 = db.Column(db.Float)
    charge_capacity = db.Column(db.Float)
    discharge_capacity_2 = db.Column(db.Float)
    net_energy_discharge = db.Column(db.Float)
    energy_charge = db.Column(db.Float)
    energy_discharge = db.Column(db.Float)
    filename = db.Column(db.String(100), nullable=False)

class DetailVoltageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer)
    step_name = db.Column(db.String(50))
    relative_time = db.Column(db.String(50))
    realtime = db.Column(db.String(50))
    auxiliary_channel_voltage = db.Column(db.Float)
    gap_of_voltage = db.Column(db.Float)
    filename = db.Column(db.String(100), nullable=False)

class DetailTemperatureData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer)
    step_name = db.Column(db.String(50))
    relative_time = db.Column(db.String(50))
    realtime = db.Column(db.String(50))
    auxiliary_channel_temperature = db.Column(db.Float)
    gap_of_temperature = db.Column(db.Float)
    filename = db.Column(db.String(100), nullable=False)

class DetailData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_index = db.Column(db.Integer)
    status = db.Column(db.String(50))
    jump_to = db.Column(db.Integer)
    cycle = db.Column(db.Integer)
    step = db.Column(db.Integer)
    cur = db.Column(db.Float)
    voltage = db.Column(db.Float)
    capacity = db.Column(db.Float)
    energy = db.Column(db.Float)
    relative_time = db.Column(db.String(50))
    absolute_time = db.Column(db.String(50))
    filename = db.Column(db.String(100), nullable=False)