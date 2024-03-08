package Main;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.SimpleFSDirectory;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.FileSystems;
import java.util.zip.GZIPInputStream;


public class DatasetIndexer {

    public static void indexDataSet(String path) throws IOException {

        GZIPInputStream gzip = new GZIPInputStream(new FileInputStream(path));
        BufferedReader br = new BufferedReader(new InputStreamReader(gzip));


        Directory dir = null;
        try {

            dir = new SimpleFSDirectory(FileSystems.getDefault().getPath("tweets_index"));

            Analyzer anal = new StandardAnalyzer();
            IndexWriterConfig cfg = new IndexWriterConfig(anal);
            IndexWriter writer = new IndexWriter(dir, cfg);

            int c = 0;
            String raw_tweet = new String();
            while ((raw_tweet = br.readLine()) != null) {
                JSONObject json_tweet = new JSONObject(raw_tweet);
                Tweet tweet = getTweet(json_tweet);
                tweet.updateDoc();
                writer.addDocument(tweet.doc);

                System.out.println("indexing tweet number " + c++);
            }

            writer.commit();
            writer.close();
            dir.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static Tweet getTweet(JSONObject json_tweet){

        Tweet tweet = new Tweet();

        tweet.Tag = ((JSONObject) json_tweet).getString("id_str");
        tweet.Created_at = ((JSONObject) json_tweet).getString("created_at");

        JSONObject json_user = ((JSONObject) json_tweet).getJSONObject("user");
        tweet.User_id = json_user.getString("id_str");
        tweet.Location = json_user.getString("location");
        tweet.Text = ((JSONObject) json_tweet).getString("text");

        try {
            tweet.Quoted_status_id = ((JSONObject) json_tweet).getString("quoted_status_id_str");
        } catch(Exception e) {
            tweet.Quoted_status_id = "";
        }

        try {
            JSONObject json_retweeted = ((JSONObject) json_tweet).getJSONObject("retweeted_status");
            tweet.Retweeted_status_id = json_retweeted.getString("id_str");
        }catch(Exception e) {
            tweet.Retweeted_status_id = "";
        }

        if(!(((JSONObject) json_tweet).get("in_reply_to_status_id_str").equals(null))){
            tweet.In_reply_to_status_id = ((JSONObject) json_tweet).getString("in_reply_to_status_id_str");
        }else{
            tweet.In_reply_to_status_id = "";
        }

        if(!(((JSONObject) json_tweet).get("in_reply_to_user_id_str").equals(null))){
            tweet.In_reply_to_user_id = ((JSONObject) json_tweet).getString("in_reply_to_user_id_str");
        }else{
            tweet.In_reply_to_user_id = "";
        }
        tweet.Retweet_count = ((JSONObject) json_tweet).getInt("retweet_count");
        tweet.Favorite_count = ((JSONObject) json_tweet).getInt("favorite_count");

        return tweet;
    }

}
