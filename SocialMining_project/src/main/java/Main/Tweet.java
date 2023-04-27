package Main;

import org.apache.lucene.document.*;

public class Tweet {

    String Tag;
    String Created_at;
    String User_id;
    String Text;
    String Location;
    String Retweeted_status_id;
    String In_reply_to_status_id;
    String Quoted_status_id;
    String In_reply_to_user_id;
    int Retweet_count;
    int Favorite_count;

    static Document doc = new Document();

    static StringField tag = new StringField("tag", "", Field.Store.YES);
    static TextField created_at = new TextField("created_at", "", Field.Store.YES);
    static StringField user_id = new StringField("user_id_str", "", Field.Store.YES);
    static TextField text = new TextField("text", "", Field.Store.YES);
    static StringField location = new StringField("location", "", Field.Store.YES);
    static StringField retweeted_status_id = new StringField("retweeted_status_id", "", Field.Store.YES);
    static StringField in_reply_to_status_id = new StringField("in_reply_to_status_id", "", Field.Store.YES);
    static StringField quoted_status_id = new StringField("quoted_status_id", "", Field.Store.YES);
    static StringField in_reply_to_user_id = new StringField("in_reply_to_user_id_str", "", Field.Store.YES);
    static IntPoint retweet_count = new IntPoint("retweet_count",0);
    static IntPoint favorite_count = new IntPoint("favorite_count",0);

    static{
        doc.add(tag);
        doc.add(created_at);
        doc.add(user_id);
        doc.add(location);
        doc.add(retweeted_status_id);
        doc.add(text);
        doc.add(in_reply_to_status_id);
        doc.add(quoted_status_id);
        doc.add(in_reply_to_user_id);
        doc.add(retweet_count);
        doc.add(favorite_count);
    }

    public void updateDoc(){
        Tweet.tag.setStringValue(Tag);
        Tweet.created_at.setStringValue(Created_at);
        Tweet.user_id.setStringValue(User_id);
        Tweet.text.setStringValue(Text);
        Tweet.location.setStringValue(Location);
        Tweet.retweeted_status_id.setStringValue(Retweeted_status_id);
        Tweet.in_reply_to_status_id.setStringValue(In_reply_to_status_id);
        Tweet.quoted_status_id.setStringValue(Quoted_status_id);
        Tweet.in_reply_to_user_id.setStringValue(In_reply_to_user_id);
        Tweet.retweet_count.setIntValue(Retweet_count);
        Tweet.favorite_count.setIntValue(Favorite_count);
    }
}
