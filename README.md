# DevNet_Marathon_GetCFG
DevNet Marathon Homework. Day 1

�������� �������:

����: ���� �� ���������� ������������ � ���������������, ��� ��� �������� �� ����� IP-�������. 
��� IP-������ ��������� ��������. ��� ����������� � �������������� �������� ��� ����������� �� IOS ��� IOS XE.

����������:
1. ������� �� ���� ��������� ����� ������������, ��������� �� �� ����, ��������� ��� ���������� � ������� ���� � ������� ����� �����.
2. ��������� �� ���� ������������ - ������� �� �������� CDP � ���� �� � �������� CDP �� ������ �� ��������� ������ � �������.
3. ���������, ����� ��� ������������ ����������� (NPE - No payload encryption ��� PE - Payload encryption) ������������ �� ����������� � ������� �� ���� ��������� ������ � ������ ������������� ��.
4. ��������� �� ���� ����������� timezone GMT+0, ��������� ������ ��� ������������� ������� �� ��������� �� ���������� ����, �������������� �������� ��� �����������.
5. ������� ����� � ���� ���������� �����, ������ �� ������� ����� ��������� ������, ������� � ������:
��� ���������� - ��� ���������� - ������ �� - NPE/PE - CDP on/off, X peers - NTP in sync/not sync.

������:
ms-gw-01|ISR4451/K9|BLD_V154_3_S_XE313_THROTTLE_LATEST |PE |CDP is ON,5 peers|Clock in Sync
ms-gw-02|ISR4451/K9|BLD_V154_3_S_XE313_THROTTLE_LATEST |NPE|CDP is ON,0 peers|Clock in Sync

--------------------------------------------------------------------------------------------

������:
- getcfg.py

������� ������:
- � csv-����� devices.csv ����� ������� ����������� ��������� ��������� � ����: host, device_type, username, password, secret
- � ������ ������������� ����� NTP-������� ���� ����� ���� ������� � ���������� NTP_SRV ������� getcfg.py

�������� ������:
- ��������� ���������� "config_backups", ������ ������� ������������ ������������ ��������� �������� � ����� csv
- � ������� ��������� ����� (������ �������� �������, ��. "������" ����)
- ������, ��������� � �������, ����������� � ���� "output.txt"
