# Faculty Workload Management System - PS No. 79

## Problem Statement
Read workload.csv with Pandas. Show total weekly hours per faculty (Limit 16 hrs/week), mark overloaded faculty, assign new subject only if limit not exceeded, and find faculty with enough free hours.

## Tech Stack
- Language: Python 3
- Library: Pandas
- Concepts: Dictionaries, Functions, File Handling

## How to Run
pip install pandas
python main.py

## Files in this Repo
- main.py - One python file with all logic
- workload.csv - Faculty data

## Test Cases Covered (As per PS)

**Test Case 1: Show workload summary**
Input: 1
Output: 
Dr. Sharma : 11 hours (5 free)
Dr. Verma : 18 hours - OVERLOADED by 2 hours
Dr. Iyer : 4 hours (12 free)

**Test Case 2: Assign subject**
Input: Dr. Sharma, Python Lab, 5 hrs
Output: Assigned. Dr. Sharma now has 16 hours (limit reached).

**Test Case 3: Invalid Cases**
(a) Dr. Sharma, Statistics, 7 hrs -> Cannot assign: would have 18 hours, exceeding 16-hour limit.
(b) Dr. Iyer, Python Lab, -2 hrs -> Hours must be a positive whole number.

**Test Case 4: Find faculty with free hours**
Input: Hours needed 8
Output: Dr. Iyer : 12 hours free

## Screenshots
Uploading test case screenshots here.
