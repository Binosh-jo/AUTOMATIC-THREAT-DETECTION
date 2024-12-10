from datetime import datetime
import pandas as pd

class AlertManager:
    def __init__(self):
        self.alerts = []
        
    def add_alert(self, alert_data):
        """Add new alert to the system"""
        alert = {
            'id': len(self.alerts) + 1,
            'timestamp': datetime.now(),
            'severity': alert_data['severity'],
            'type': alert_data['type'],
            'description': alert_data['description'],
            'source': alert_data.get('source', 'Unknown'),
            'status': 'New'
        }
        self.alerts.append(alert)
        return alert
        
    def get_alerts(self, start_time, end_time):
        """Get alerts within time period"""
        return [
            alert for alert in self.alerts
            if start_time <= alert['timestamp'] <= end_time
        ]
        
    def get_recent_alerts(self, limit=10):
        """Get most recent alerts"""
        return sorted(
            self.alerts,
            key=lambda x: x['timestamp'],
            reverse=True
        )[:limit]
        
    def get_average_response_time(self):
        """Calculate average response time"""
        response_times = []
        for alert in self.alerts:
            if alert.get('resolved_at'):
                response_time = alert['resolved_at'] - alert['timestamp']
                response_times.append(response_time.total_seconds())
        return sum(response_times) / len(response_times) if response_times else 0 