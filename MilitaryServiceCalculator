from datetime import datetime, timedelta

def calculate_dates(enlist_date, end_of_service_date, relationship_start_date):
    enlist_date = datetime.strptime(enlist_date, "%Y-%m-%d")
    end_of_service_date = datetime.strptime(end_of_service_date, "%Y-%m-%d")
    relationship_start_date = datetime.strptime(relationship_start_date, "%Y-%m-%d")

    service_days = (end_of_service_date - enlist_date).days

    pre_enlist_days = (enlist_date - relationship_start_date).days

    total_days = (datetime.now() - relationship_start_date).days

    days_together = total_days - service_days
    days_waited = service_days - pre_enlist_days

    total_service_days = (end_of_service_date - enlist_date).days

    remaining_service_days = (end_of_service_date - datetime.now()).days

    return service_days, pre_enlist_days, total_days, days_together, days_waited, total_service_days, remaining_service_days

enlist_date = input("입대 날짜를 입력하세요 (예: 2022-01-01): ")
end_of_service_date = input("전역 날짜를 입력하세요 (예: 2023-01-01): ")
relationship_start_date = input("연애 시작 날짜를 입력하세요 (예: 2021-01-01): ")

service_days, pre_enlist_days, total_days, days_together, days_waited, total_service_days, remaining_service_days = calculate_dates(enlist_date, end_of_service_date, relationship_start_date)

print(f"군 복무일수: {service_days}일")
print(f"입대 전 교제일수: {pre_enlist_days}일")
print(f"전체 교제일수: {total_days}일")
print(f"함께한지: {days_together}일")
print(f"기다린지: {days_waited}일")
print(f"총 복무일수: {total_service_days}일")
print(f"남은 복무일수: {remaining_service_days}일")
