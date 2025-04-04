

echo "=== Starting Flask App ==="

cd /home/ubuntu/myflaskapp

# Kill any running app.py process
pkill -f app.py || true

# Run the Flask app in the background
nohup python3 app.py > app.log 2>&1 &
