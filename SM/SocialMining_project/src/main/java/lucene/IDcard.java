package lucene;

import org.apache.lucene.document.*;

public class IDcard {

    String Tag;
    String Name;
    Double Height;
    Long Bdate;
    String Bio;


    static Document doc = new Document();

    static StringField tag = new StringField("tag", "", Field.Store.YES);
    static TextField name = new TextField("name", "", Field.Store.YES);
    static DoublePoint height = new DoublePoint("height",0.0);
    static StringField bio = new StringField("bio", "", Field.Store.YES);
    static LongPoint bdate = new LongPoint("bdate", 0L); // no storage default
    // static StoredField bdate = new StoredField("bdate", 26121998L); // stored long field

    static{
        doc.add(tag);
        doc.add(name);
        doc.add(bdate);
        doc.add(height);
        doc.add(bio);
    }

    public void updateDoc(){
        lucene.IDcard.tag.setStringValue(Tag);
        lucene.IDcard.name.setStringValue(Name);
        lucene.IDcard.height.setDoubleValue(Height);
        lucene.IDcard.bdate.setLongValue(Bdate);
        lucene.IDcard.bio.setStringValue(Bio);

    }



}
