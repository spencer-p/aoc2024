package main

import (
	"bytes"
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"regexp"
	"time"
)

var token = os.Getenv("AOC_TOKEN")

func main() {
	day := flag.Int("day", -1, "The day of December to download")
	year := flag.Int("year", 2024, "The year to download")
	flag.Parse()
	now := time.Now()
	if *day == -1 {
		*day = now.Day() + 1
	}

	// Calculate 9PM for the requested day and possibly wait for it.
	today9PM := time.Date(now.Year(), now.Month(), *day-1, 21, 0, 0, 0, now.Location())
	wait := time.Until(today9PM)
	if wait > 0 {
		log.Printf("Waiting %s until 9pm", wait)
		<-time.After(wait)
	}

	// Fetch the input
	path := fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", *year, *day)
	body, err := get(path)
	if err != nil {
		log.Fatalf("download input.txt: %v", err)
	}

	out, err := os.Create("input.txt")
	if err != nil {
		log.Fatalf("create input.txt; %v", err)
	}
	defer out.Close()

	n, err := io.Copy(out, body)
	if err != nil {
		log.Fatalf("write input.txt: %v", err)
	}
	log.Printf("input.txt done (%d bytes)", n)

	// Fetch problem statement and extract the example
	path = fmt.Sprintf("https://adventofcode.com/%d/day/%d", *year, *day)
	body, err = get(path)
	if err != nil {
		log.Fatalf("download problem statement: %v", err)
	}
	defer body.Close()
	statement, err := io.ReadAll(body)
	if err != nil {
		log.Fatalf("failed to read body of statement: %v", err)
	}

	out, err = os.Create("input2.txt")
	if err != nil {
		log.Fatalf("create input2.txt; %v", err)
	}
	defer out.Close()

	r := regexp.MustCompile(`(?sU)For example[^:]*:.*<code>(.*)</code>`)
	example := r.FindSubmatch(statement)
	if example == nil {
		io.Copy(out, bytes.NewBuffer(statement))
		log.Fatalf("failed to find example, wrote full text")
	}
	n, err = io.Copy(out, bytes.NewBuffer(example[1]))
	if err != nil {
		log.Fatalf("write input2.txt: %v", err)
	}
	log.Printf("input2.txt done (%d bytes)", n)

}

func get(path string) (io.ReadCloser, error) {
	req, err := http.NewRequest(http.MethodGet, path, nil)
	if err != nil {
		return nil, err
	}
	req.AddCookie(&http.Cookie{
		Name:  "session",
		Value: token,
	})

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, err
	}
	if resp.StatusCode != http.StatusOK {
		dump, _ := io.ReadAll(resp.Body)
		log.Printf("%s", dump)
		return nil, fmt.Errorf("bad status code %d", resp.StatusCode)
	}
	return resp.Body, nil
}
