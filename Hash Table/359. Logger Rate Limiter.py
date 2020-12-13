"""
359. Logger Rate Limiter
Hash Table

Description:
Design a logger system that receive stream of messages along with its timestamps, 
each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.

Example:
Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""

# Solution:
class Solution(object):
    def shouldPrintMessage(self, message, timestamp):
        """
        Method: Create a dictionary to hold the message and its time stamp.
                If the message has never been seen before or it doesn't show up in the last 10 steps, return true.
                Otherwise, return false.
        """
        
        logger = {}
        if message not in logger or timestamp - logger[message] >= 10:
            logger[message] = timestamp
            return True
        else:
            return False

