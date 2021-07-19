using System;
using System.Linq;
using System.Collections.Generic;

namespace Tools
{
    class Program
    {
        static void Main(string[] args)
        {
            Program p = new Program(1000);
            var primes = p.Calculate(100);
            int total = primes.Sum();
            Console.WriteLine(total);
        }

        private readonly int wheelSize;

        public Program(int wheelSize) {
            this.wheelSize = wheelSize;
        }

        public IEnumerable<int> Calculate(int numberOfPrimes) {
            List<int> primes = new List<int> { 2 };
            List<int> factors = new List<int> { 2 };
            bool[] wheel = new bool[this.wheelSize];
            int wheelStart = 2;

            while(true) {
                for (int i = 0; i < primes.Count; i++) {
                    int prime = primes[i];
                    int factor = factors[i];
                    while (factor - wheelStart < wheel.Length) {
                        wheel[factor - wheelStart] = true;
                        factor += prime;
                        factors[i] = factor;
                    }
                }

                for (int i = 0; i < wheel.Length; i++) {
                    bool isPrime = !wheel[i];
                    if (isPrime) {
                        int prime = i + wheelStart;
                        if (prime > 2000000) {
                            return primes;
                        }

                        primes.Add(prime);
                        factors.Add(prime);

                        // if (primes.Count >= numberOfPrimes) {
                        //     return primes;
                        // }

                        int j = primes.Count - 1;

                        // Wheel the prime forward.
                        int factor = factors[j];
                        while (factor - wheelStart < wheel.Length) {
                            wheel[factor - wheelStart] = true;
                            factor += prime;
                            factors[j] = factor;
                        }
                    }
                }

                // extend the wheel
                wheelStart += wheelSize;
                for (int i=0; i<wheelSize; i++) wheel[i] = false;
            }
        }
    }
}