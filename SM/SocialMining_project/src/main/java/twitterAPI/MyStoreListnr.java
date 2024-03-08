package twitterAPI;

import twitter4j.*;

public class MyStoreListnr implements StatusListener {

    public void onStatus(Status status) {
        System.out.println(TwitterObjectFactory.getRawJSON(status));
    }

    public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) { }
    public void onTrackLimitationNotice(int i) { }
    public void onScrubGeo(long l, long l1) { }
    public void onStallWarning(StallWarning stallWarning) { }
    public void onException(Exception e) { }
}
