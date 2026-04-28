import socket  # المكتبة المسؤولة عن الاتصالات والشبكات
from datetime import datetime

def port_scanner(target_ip):
    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Scanning started at: {str(datetime.now())}")
    print("-" * 50)

    # قائمة بالمنافذ الشائعة لفحصها (مثلاً: 21, 22, 80, 443)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3389]

    try:
        for port in common_ports:
            # إنشاء "سوكت" للاتصال عبر بروتوكول TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # ضبط وقت الانتظار لثانية واحدة عشان السرعة
            socket.setdefaulttimeout(1)
            
            # محاولة الاتصال بالمنفذ
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting program...")
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved.")
    except socket.error:
        print("\n Server not responding.")

# تشغيل البرنامج
if __name__ == "__main__":
    # تقدر تحط IP جهازك أو موقع للتجربة (تأكد إنه مصرح لك بفحصه)
    target = input("Enter the IP address to scan: ")
    port_scanner(target)
