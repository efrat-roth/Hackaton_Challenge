import React from 'react';
import './Events.css';

function Events() {
  const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  const getCurrentMonth = () => {
    const currentDate = new Date();
    return currentDate.getMonth();
  };

  const getCurrentYear = () => {
    const currentDate = new Date();
    return currentDate.getFullYear();
  };

  const renderCalendar = () => {
    const month = getCurrentMonth();
    const year = getCurrentYear();

    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const calendarDays = [];
    const eventsData = [
      { day: 5, events: ['Event 1', 'Event 2'] },
      { day: 10, events: ['Event 3'] },
      { day: 15, events: ['Event 4', 'Event 5', 'Event 6'] },
    ];

    // יצירת הימים בלוח השנה
    for (let day = 1; day <= daysInMonth; day++) {
      const events = eventsData.find((item) => item.day === day)?.events;

      calendarDays.push(
        <div key={day} className="calendar-day">
          <div className="day-number">{day}</div>
          {events && (
            <ul className="events-list">
              {events.map((event, index) => (
                <li key={index} className="event-item">
                  {event}
                </li>
              ))}
            </ul>
          )}
        </div>
      );
    }

    // הוספת ימים ריקים לפני החודש
    for (let i = 0; i < firstDayOfMonth; i++) {
      calendarDays.unshift(<div key={`empty-${i}`} className="calendar-day empty"></div>);
    }

    return calendarDays;
  };

  return (
    <div className="events-container">
      <h2>{months[getCurrentMonth()]}</h2>
      <div className="calendar">{renderCalendar()}</div>
    </div>
  );
}

export default Events;