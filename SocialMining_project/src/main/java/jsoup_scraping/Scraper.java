package jsoup_scraping;

import org.jsoup.*;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.net.SocketTimeoutException;
import java.util.ArrayList;

public class Scraper{
    public static final String USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0";
    private String baseurl;

    public static void main(String[] args) throws Throwable{
        Scraper crawler = new Scraper();

        crawler.baseurl = "https://www.romatoday.it";
        String landing = crawler.baseurl + "/eventi/";

        Document doc = null;
        ArrayList<Event> events = new ArrayList<>();

        if((doc = crawler.fetch(landing)) != null){
            crawler.extractBaseInfo(doc, events);
        }

        for(Event e: events){
            e.printToOut();
        }
    }

    public Document fetch(String url) throws IOException {
        Document webpage = null;
        try{
            webpage = Jsoup.connect(url).userAgent(USER_AGENT).get();
            System.out.println("pagina scaricata: " + url);
            return webpage;
        }catch (HttpStatusException e){
            System.out.println(e.getStatusCode());
        }catch (SocketTimeoutException e){
            System.out.println("socket timeout");
        }
        return null;
    }

    public void extractBaseInfo(Document doc, ArrayList<Event> events){

        System.out.println("extracting base info... ");

        Elements heds = doc.select(".block__heading .link");
        Elements dates = doc.select("span.text-sm:nth-child(2)");
        Elements places = doc.select(".text-sm a");
        // puoi prendere altre info ...

        for(int i = 0; i < heds.size(); i++ ){
            Event e = new Event();
            e.Url = baseurl + heds.get(i).attr("href");

            e.Name = heds.get(i).text();
            e.Date = dates.get(i).text();
            e.Place =  places.get(i).text();
            // basta info, grazie, ciao...

            events.add(e);
        }
    }

}
