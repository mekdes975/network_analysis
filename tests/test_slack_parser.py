import os
import sys
import unittest

import numpy

current_script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_script_directory, os.pardir))

sys.path.append(parent_directory)

from src.loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):
    """Unit tests for the SlackDataLoader class."""

    def setUp(self):
        """Initialize paths for testing."""
        self.slack_data_path = 'Anonymized_B6SlackExport_25Nov23/anonymized/'
        self.channel_path = 'Anonymized_B6SlackExport_25Nov23/anonymized/all-community-building/'

    def test_slack_parser_column(self):
        """Test the column names generated by the slack_parser method."""
        expected_column_names = ['msg_type', 'msg_content', 'sender_name',
                                 'msg_sent_time', 'msg_dist_type', 'time_thread_start',
                                 'reply_count', 'reply_users_count', 'reply_users',
                                 'tm_thread_end', 'channel']

        df = SlackDataLoader(self.slack_data_path).slack_parser(self.channel_path)
        actual_column_names = list(df.columns)

        self.assertEqual(actual_column_names, expected_column_names)

    
if __name__ == '__main__':
    unittest.main()