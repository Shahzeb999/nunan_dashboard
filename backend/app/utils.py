import pandas as pd
from app import db
from app.models import CycleData, StatisticsData, DetailVoltageData, DetailTemperatureData, DetailData, CellData, Cell
import os

def process_excel_file(file_path):
    filename = os.path.basename(file_path)
    xls = pd.read_excel(file_path, sheet_name=None)
    sheet_names = xls.keys()
    print(sheet_names)  # Debug: Print sheet names

    # Process Cycle Data
    cycle_sheets = [name for name in sheet_names if 'Cycle' in name]
    for cycle_sheet in cycle_sheets:
        print(f"Processing sheet: {cycle_sheet}")  # Debug: Sheet being processed
        process_cycle_data(xls[cycle_sheet], filename)

    # Process Statistics Data
    statis_sheets = [name for name in sheet_names if 'Statis' in name]
    for statis_sheet in statis_sheets:
        print(f"Processing sheet: {statis_sheet}")  # Debug: Sheet being processed
        process_statistics_data(xls[statis_sheet], filename)

    # Process Detail Voltage Data
    detail_vol_sheets = [name for name in sheet_names if 'DetailVol' in name]
    for detail_vol_sheet in detail_vol_sheets:
        print(f"Processing sheet: {detail_vol_sheet}")  # Debug: Sheet being processed
        process_detail_voltage_data(xls[detail_vol_sheet], filename)

    # Process Detail Temperature Data
    detail_temp_sheets = [name for name in sheet_names if 'DetailTemp' in name]
    for detail_temp_sheet in detail_temp_sheets:
        print(f"Processing sheet: {detail_temp_sheet}")  # Debug: Sheet being processed
        process_detail_temperature_data(xls[detail_temp_sheet], filename)

    # Process Detail Data
    detail_sheets = [name for name in sheet_names if 'Detail' in name and 'Vol' not in name and 'Temp' not in name]
    for detail_sheet in detail_sheets:
        print(f"Processing sheet: {detail_sheet}")  # Debug: Sheet being processed
        print(xls[detail_sheet].columns)  # Debug: Print column names
        process_detail_data(xls[detail_sheet], filename)

def process_cycle_data(sheet, filename):
    for _, row in sheet.iterrows():
        cycle_data = CycleData(
            channel=int(row['Channel']),
            total_cycle=int(row['ToTal of Cycle']),
            charge_capacity=float(row['Capacity of charge(mAh)']),
            discharge_capacity=float(row['Capacity of discharge(mAh)']),
            cycle_life=float(row['Cycle Life(%)']),
            filename=filename
        )
        print(cycle_data)  # Debug: Print data being added
        db.session.add(cycle_data)
    db.session.commit()

def process_statistics_data(sheet, filename):
    for _, row in sheet.iterrows():
        statistics_data = StatisticsData(
            channel=int(row['Channel']),
            cycle=int(row['CyCle']),
            step=int(row['Step']),
            status=row['Status'],
            start_voltage=float(row['Start Voltage(V)']),
            end_voltage=float(row['End Voltage(V)']),
            start_current=float(row['Start Current(mA)']),
            end_current=float(row['End Current(mA)']),
            capacity=float(row['CapaCity(mAh)']),
            endure_time=row['Endure Time(h:min:s.ms)'],
            relative_time=row['Relative Time(h:min:s.ms)'],
            absolute_time=row['Absolute Time'],
            discharge_capacity_1=float(row['Discharge_Capacity(mAh)']),
            charge_capacity=float(row['Charge_Capacity(mAh)']),
            discharge_capacity_2=float(row['Discharge_Capacity(mAh)']),
            net_energy_discharge=float(row['Net Engy_DChg(mWh)']),
            energy_charge=float(row['Engy_Chg(mWh)']),
            energy_discharge=float(row['Engy_DChg(mWh)']),
            filename=filename
        )
        print(statistics_data)  # Debug: Print data being added
        db.session.add(statistics_data)
    db.session.commit()

def process_detail_voltage_data(sheet, filename):
    for _, row in sheet.iterrows():
        detail_voltage_data = DetailVoltageData(
            record_id=int(row['Record ID']),
            step_name=row['Step Name'],
            relative_time=row['Relative Time(h:min:s.ms)'],
            realtime=row['Realtime'],
            auxiliary_channel_voltage=float(row['Auxiliary channel TU1 U(V)']),
            gap_of_voltage=float(row['Gap of Voltage']),
            filename=filename
        )
        print(detail_voltage_data)  # Debug: Print data being added
        db.session.add(detail_voltage_data)
    db.session.commit()

def process_detail_temperature_data(sheet, filename):
    for _, row in sheet.iterrows():
        detail_temperature_data = DetailTemperatureData(
            record_id=int(row['Record ID']),
            step_name=row['Step Name'],
            relative_time=row['Relative Time(h:min:s.ms)'],
            realtime=row['Realtime'],
            auxiliary_channel_temperature=float(row['Auxiliary channel TU1 T(°C)']),
            gap_of_temperature=float(row['Gap of Temperature']),
            filename=filename
        )
        print(detail_temperature_data)  # Debug: Print data being added
        db.session.add(detail_temperature_data)
    db.session.commit()

def process_detail_data(sheet, filename):
    print(sheet.columns)  # Debug: Print column names
    for _, row in sheet.iterrows():
        detail_data = DetailData(
            record_index=int(row['Record Index']),
            status=row['Status'],
            jump_to=int(row['JumpTo']),
            cycle=int(row['Cycle']),
            step=int(row['Step']),
            cur=float(row['Cur(mA)']),
            voltage=float(row['Voltage(V)']),
            capacity=float(row['CapaCity(mAh)']),
            energy=float(row['Energy(mWh)']),
            relative_time=row['Relative Time(h:min:s.ms)'],
            absolute_time=row['Absolute Time'],
            filename=filename
        )
        print(detail_data)  # Debug: Print data being added
        db.session.add(detail_data)
    db.session.commit()
