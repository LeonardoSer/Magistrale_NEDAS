package jsoup_scraping;

public class Event {
    String Url;
    String Name;
    String Date;
    String Place;
    String Price;
    String Info;
    String Body;
    String title;

    public void printToOut(){
        System.out.println();
        System.out.println( "Url: " + Url);
        System.out.println( "Name: " + Name);
        System.out.println( "Date: " + Date);
        System.out.println( "Place: " + Place);
        System.out.println( "Price: " + Price);
        System.out.println( "Info: " + Info);
        System.out.println( "Body: " + Body);
        System.out.println( "title: " + title);
    }
}
