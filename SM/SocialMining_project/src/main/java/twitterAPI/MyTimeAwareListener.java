package twitterAPI;

import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;

public class MyTimeAwareListener implements StatusListener{

    private long last = -1;
    private long counter = 0;

    private long delta = 10*1000; // 10 secondi

    @Override
    public void onStatus(Status status) {
        long current = status.getCreatedAt().getTime();

        if(last == -1){
            last = current;
        }
        if(current - last >= delta){
            System.out.println(counter);
            last = current;
            counter = 1;
        }else
            counter ++;
    }

    @Override
    public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice){}
    @Override
    public void onTrackLimitationNotice(int i){}
    @Override
    public void onScrubGeo(long l, long l1){}
    @Override
    public void onStallWarning(StallWarning stallWarning){}
    @Override
    public void onException(Exception e){}
}
