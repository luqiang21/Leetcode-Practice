// Write a function mergeRanges() that takes a vector of multiple meeting time
// ranges and returns a vector of condensed ranges.

#include <vector>
#include <iostream>
using namespace std;

class Meeting
{
private:
    // number of 30 min blocks past 9:00 am
    unsigned int startTime_;
    unsigned int endTime_;

public:
    Meeting() :
        startTime_(0),
        endTime_(0)
    {
    }

    Meeting(unsigned int startTime, unsigned int endTime) :
        startTime_(startTime),
        endTime_(endTime)
    {
    }

    unsigned int getStartTime() const
    {
        return startTime_;
    }

    void setStartTime(unsigned int startTime)
    {
        startTime_ = startTime;
    }

    unsigned int getEndTime() const
    {
        return endTime_;
    }

    void setEndTime(unsigned int endTime)
    {
        endTime_ = endTime;
    }

    bool operator==(const Meeting& other) const
    {
        return
            startTime_ == other.startTime_
            && endTime_ == other.endTime_;
    }

    bool operator< (const Meeting& other) const
    {
        return startTime_ < other.startTime_;
    }
};


// my method
vector<Meeting> merge_ranges(vector<Meeting> meetings) {
    if(meetings.size() <= 1) {
        return meetings;
    }
    vector<Meeting> res;

    sort(meetings.begin(), meetings.end());
    res.push_back(meetings[0]);
    for(int i = 0; i < meetings.size(); ++i) {
        Meeting new_meeting = meetings[i];
        Meeting *plast_meeting = &res.back();
        if(new_meeting.getStartTime() > plast_meeting -> getEndTime()) {
            res.push_back(new_meeting);

        }
        else {
            unsigned int endTime = max(plast_meeting -> getEndTime(), new_meeting.getEndTime());

            plast_meeting -> setEndTime(endTime);

        }
    }
    return res;
}

// answer from the IC
bool compareMeetingsByStartTime(
  const Meeting& firstMeeting,
  const Meeting& secondMeeting)
{
  return firstMeeting.getStartTime() < secondMeeting.getStartTime();
}

vector<Meeting> merge_ranges1(const vector<Meeting>& meetings)
{
  // sort by start time
  vector<Meeting> sortedMeetings(meetings);
  sort(sortedMeetings.begin(), sortedMeetings.end(), compareMeetingsByStartTime);

  // initialize mergedMeetings with the earliest meeting
  vector<Meeting> mergedMeetings;
  mergedMeetings.push_back(sortedMeetings.front());

  for (const Meeting& currentMeeting : sortedMeetings) {
      Meeting& lastMergedMeeting = mergedMeetings.back();

      if (currentMeeting.getStartTime()
              <= lastMergedMeeting.getEndTime()) {
          // if the current meeting overlaps with the last merged meeting, use the
          // later end time of the two
          lastMergedMeeting.setEndTime(max(lastMergedMeeting.getEndTime(),
              currentMeeting.getEndTime()));
      }
      else {
          // add the current meeting since it doesn't overlap
          mergedMeetings.push_back(currentMeeting);
      }
  }

  return mergedMeetings;
}

int main() {
    vector<Meeting> meetings = {Meeting(0, 1), Meeting(3, 5), Meeting(4, 8), Meeting(10, 12), Meeting(9, 10)};

    vector<Meeting> res = merge_ranges(meetings);
    vector<Meeting>::iterator it = res.begin();
    while(it != res.end()) {
        cout << it -> getStartTime() << "  " << it -> getEndTime() << endl;
        it ++;
    }

    cout << endl;
    res = merge_ranges1(meetings);
    it = res.begin();
    while(it != res.end()) {
        cout << it -> getStartTime() << "  " << it -> getEndTime() << endl;
        it ++;
    }
    return 0;
}
