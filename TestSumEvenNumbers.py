import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestSumEvenNumbers {

    @Test
    public void testSum() {
        // Redirect System.out to capture the program output
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // Call the main method of the student's program
        SumEvenNumbers.main(new String[]{});

        // Expected output
        String expectedOutput = "Sum of even numbers from 1 to 100: 2550";

        // Check if the output matches the expected result exactly
        assertEquals(expectedOutput, outContent.toString().trim());
    }
}
