const X: string[] = ['1', '2', '3', '4', '5', '6'];
const Y: string[] = ['u', 'v', 'x', 'y', 'z'];
const adj: Record<string, string[]> = {
  '1': ['x', 'z'],
  '2': ['x', 'y'],
  '3': ['u', 'v'],
  '4': ['x', 'y'],
  '5': ['u', 'x'],
  '6': ['y', 'z'],
  'u': ['3', '5'],
  'v': ['3'],
  'x': ['1', '2', '4', '5'],
  'y': ['2', '4', '6'],
  'z': ['1', '6'],
};
const M: Record<string, string> = {
  '1': 'z',
  '3': 'u',
  '4': 'x',
  '6': 'y',
  'u': '3',
  'x': '4',
  'y': '6',
  'z': '1',
};
// the set of vertices in X that are not matched
const Ux = X.filter(x => !M[x]);

function bfsAugmentingPath(): string[] | undefined {
  let P = [];
  let visited = [];
  let L = ['2', '5'];
  visited.push(L);

  let pred: Record<string, string> = {};

  console.log(`L = ${L}`);

  while (L.length > 0) {
    let a = L.shift()!;
    console.log(`a = ${a}`);
    console.log(`L = ${L}`);

    if (X.includes(a)) {
      console.log(`X includes ${a}`);
      for (let b of adj[a]!) {
        if (M[a] === b) {
          continue;
        }

        if (visited.includes(b)) {
          continue;
        }

        console.log(`b = ${b}`);

        visited.push(b);
        console.log(`visited ${b}`);
        pred[b] = a;
        console.log(`pred[${b}] = ${a}`);

        if (M[b]) {
          console.log(`${b} is in M`);
          L.push(b);
          console.log(`L = ${L}`);
        } else {
          console.log(`${b} is not in M`);
          P = [b];
          console.log(`P = ${P}`);
          let c = b;
          console.log(`c = ${c}`);
          while (!Ux.includes(c)) {
            let d = pred[c]!;
            console.log(`d = ${d}`);
            c = d;
            console.log(`c = ${c}`);
            P.unshift(c);
            console.log(`P = ${P}`);
          }
          console.log(`path found`);
          return P;
        }
      }
    } else {
      console.log(`X does not include ${a}`);
      let b = M[a]!;
      console.log(`b = ${b}`);
      visited.push(b);
      console.log(`visited ${b}`);
      pred[b] = a;
      console.log(`pred[${b}] = ${a}`);
      L.push(b);
      console.log(`L = ${L}`);
    }
  }
}

bfsAugmentingPath();
