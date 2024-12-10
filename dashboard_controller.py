import sys
import os
from datetime import datetime, timedelta
import pandas as pd

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.alert_manager import AlertManager
from models.report_generator import ReportGenerator
from threat_detection import ThreatDetector
from data_processing import DataProcessor

class DashboardController:
    def __init__(self):
        self.alert_manager = AlertManager()
        self.report_generator = ReportGenerator()
        self.threat_detector = ThreatDetector()
        self.data_processor = DataProcessor()
        
    def get_threat_summary(self, time_period='24h'):
        """Get summary of threats for dashboard"""
        return self.report_generator.get_threat_summary()
        
    def get_recent_alerts(self, limit=10):
        """Get most recent alerts"""
        return self.alert_manager.get_recent_alerts(limit)
        
    def get_threat_analysis(self):
        """Get threat analysis data"""
        return self.threat_detector.get_analysis_summary()
        
    def generate_report(self, report_type='summary'):
        """Generate system report"""
        return self.report_generator.generate_report(report_type)
        
    def get_system_metrics(self):
        """Get system performance metrics"""
        return {
            'detection_rate': self.threat_detector.get_detection_rate(),
            'false_positive_rate': self.threat_detector.get_false_positive_rate(),
            'response_time': self.alert_manager.get_average_response_time()
        } 