public class Printer {

    private int remainingPaper;
    private int tonerLevel;

    public Printer(int remainingPaper, int tonerLevel) {
        this.remainingPaper = remainingPaper;
        this.tonerLevel = tonerLevel;
    }

    public int getRemainingPaper() {
        return this.remainingPaper;
    }

    public int getTonerLevel() {
        return this.tonerLevel;
    }

    public void print(int pages, int copies) {
        int totalPages = pages * copies;
        if (this.getTonerLevel() > totalPages) {
            this.tonerLevel = this.tonerLevel - totalPages;
        } else {
            while (this.getTonerLevel() > 0) {
                this.tonerLevel--;

            }
        }
        if (totalPages <= this.getRemainingPaper()) {
            this.remainingPaper = this.remainingPaper - totalPages;
        }
    }
}
