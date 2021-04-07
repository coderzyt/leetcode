package multithread;

import java.util.Date;

public class Event {

    private Date date;

    private String event;

    public void setDate(Date date) {
        this.date = date;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public Date getDate() {
        return this.date;
    }

    public String getEvent() {
        return this.event;
    }
}
