package twitterAPI;

import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;

import java.io.IOException;
import java.util.Arrays;
import java.util.Map;

public class TwitterAPITest {
    public static void main( String[] args ) throws TwitterException, IOException, InterruptedException {

        // configurations
        ConfigurationBuilder cfg = new ConfigurationBuilder();
        cfg.setJSONStoreEnabled(true); // permette di accedere all'originale json dei tweet
        {
            cfg.setOAuthAccessToken("1370005637208346626-rAzXgV35v3th5CRDyRPDRwKiWfQPpS");
            cfg.setOAuthAccessTokenSecret("ChMWmqZ5dYlQjTg1Esif2T927HdI2wufC9BH8qqYDB3Vw");
            cfg.setOAuthConsumerKey("xRAeZV3kAJu6VmBbgFxRvAzSL");
            cfg.setOAuthConsumerSecret("bGELwwzmhfKNp2xfD3xcGJluLygk7cVI9k4yqH14UbimCcDK8D");
        }

        // twitter object
        Twitter twitter = new TwitterFactory(cfg.build()).getInstance();

        // prendiamo gli id dei following e dei follower di Repubblica
        long accountID = 18935802L;

        long [] followingsIDs = twitter.getFriendsIDs(accountID, -1).getIDs();
        System.out.println(Arrays.toString(followingsIDs));

        long [] followersIDs = twitter.getFollowersIDs(accountID, -1).getIDs();
        System.out.println(Arrays.toString(followersIDs));

        // conteggio delle chiamate residue e del tempo rimanente al reset
        Map<String, RateLimitStatus> limit = twitter.getRateLimitStatus();
        System.out.println("remaining /friends/ids call: " + limit.get("/friends/ids").getRemaining());
        System.out.println("    -> time to wait: " + limit.get("/friends/ids").getSecondsUntilReset());

        System.out.println("remaining /followers/ids call: " + limit.get("/followers/ids").getRemaining());
        System.out.println("    -> time to wait: " + limit.get("/followers/ids").getSecondsUntilReset());

    }

    }
