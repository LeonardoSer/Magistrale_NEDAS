package twitterAPI;

import twitter4j.*;

import java.util.Locale;

public class MyFilterListnr implements StatusListener {

    public void onStatus(Status status) {
        if(status.getText().toLowerCase().contains("pene")){
            System.out.println(status.getUser().getName() + " > " + status.getText());
        }
    }

    public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) { }
    public void onTrackLimitationNotice(int i) { }
    public void onScrubGeo(long l, long l1) { }
    public void onStallWarning(StallWarning stallWarning) { }
    public void onException(Exception e) { }
}

