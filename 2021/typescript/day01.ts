import * as fs from 'fs'

if (process.argv.length !== 3) {
  console.error(`usage: node ${process.argv[1]} FILENAME`)
  process.exit(1)
}

function solve(input: number[]): number {
  let prev = input[0]
  let count = 0
  for (const item of input.slice(1)) {
    if (prev < item) {
      count += 1
    }
    prev = item
  }
  return count
}

const input = fs
  .readFileSync(process.argv[2], 'utf-8')
  .trim()
  .split(/\r?\n/)
  .map((s: string) => parseInt(s, 10))

console.log(solve(input))
