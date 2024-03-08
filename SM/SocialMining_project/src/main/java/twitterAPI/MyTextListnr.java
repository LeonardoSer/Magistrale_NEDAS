package twitterAPI;

import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;

public class MyTextListnr implements StatusListener {

    public void onStatus(Status status) {
        System.out.println(status.getUser().getName() + " > " + status.getText());
    }

    public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) { }
    public void onTrackLimitationNotice(int i) { }
    public void onScrubGeo(long l, long l1) { }
    public void onStallWarning(StallWarning stallWarning) { }
    public void onException(Exception e) { }
}
