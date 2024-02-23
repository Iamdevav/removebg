# from app import create_app
 
# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
import signal
import sys
from app import create_app

def signal_handler(sig, frame):
    print('Received SIGTERM signal. Exiting gracefully.')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_handler)
    
    app = create_app()
    app.run(debug=True)
