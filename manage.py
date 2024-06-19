inport os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_comand_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and"
                "avaible on your PYTHONPATH enviroment variable? Did you"
                "forget to activate a virtual env?"
            ) from exc
        execute_from_command_line(sys.argv)

        if __name__ == '__main__':
            main()
