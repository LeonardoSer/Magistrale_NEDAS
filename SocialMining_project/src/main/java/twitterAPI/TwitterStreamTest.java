package twitterAPI;

import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;

import java.io.IOException;

// API Key: xRAeZV3kAJu6VmBbgFxRvAzSL
// API Secret Key: bGELwwzmhfKNp2xfD3xcGJluLygk7cVI9k4yqH14UbimCcDK8D

// Access Token: 1370005637208346626-rAzXgV35v3th5CRDyRPDRwKiWfQPpS
// Access Token secret: ChMWmqZ5dYlQjTg1Esif2T927HdI2wufC9BH8qqYDB3Vw

public class TwitterStreamTest {
    public static void main( String[] args ) throws TwitterException, IOException {

        // configurations
        ConfigurationBuilder cfg = new ConfigurationBuilder();
        cfg.setJSONStoreEnabled(true);
        {
            // permette di accedere all'originale json dei tweet
            cfg.setOAuthAccessToken("1370005637208346626-rAzXgV35v3th5CRDyRPDRwKiWfQPpS");
            cfg.setOAuthAccessTokenSecret("ChMWmqZ5dYlQjTg1Esif2T927HdI2wufC9BH8qqYDB3Vw");
            cfg.setOAuthConsumerKey("xRAeZV3kAJu6VmBbgFxRvAzSL");
            cfg.setOAuthConsumerSecret("bGELwwzmhfKNp2xfD3xcGJluLygk7cVI9k4yqH14UbimCcDK8D");
        }

        // stream Object
        TwitterStream stream = new TwitterStreamFactory(cfg.build()).getInstance();

        // vari listener
        StatusListener textListener = new MyTextListnr();
        StatusListener storeListener = new MyStoreListnr();
        StatusListener timeAwareListnr = new MyTimeAwareListener();

        // risultati testuali
        /*
        stream.addListener(textListener);
        stream.sample(); // prende l'1% dei tweet totali, e chiama il listener associato in continuazione
         */

        // Risultati in Json
        /*
        stream.addListener(storeListener);
        stream.sample();
         */


        // post filtraggio
        /*
        stream.addListener(textListener);
        stream.sample(); // sempre il textbased di prima
        FilterQuery fq = new FilterQuery();
        String[] queryText = {"nigga"};
        fq.track(queryText);
        stream.filter(fq); // chiama il listener associato e poi filtra sull' 1% dei tweet
         */

        // filtraggio e conteggio dei risultati
        stream.addListener(timeAwareListnr);
        stream.sample(); // prende l'1% dei tweet totali, e chiama il listener associato in continuazione
        FilterQuery fq = new FilterQuery();
        String[] queryText = {"nigga"};
        fq.track(queryText);
        stream.filter(fq); //filtra sullo stream (1%) e chiama il listener associato

        // pre filtraggio -> va fatto nel listener
        /*
        StatusListener filterListener = new MyFilterListnr();
        stream.addListener(filterListener);
        stream.sample();
         */
    }
}
